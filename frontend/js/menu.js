var MenuModel = function() {
    var self = this;

    self.user = ko.observable("default");
    self.userName = ko.observable();

    self.currentView = ko.observable("landing");

    self.vNoSelected = ko.observable();
    self.rNoSelected = ko.observable();


    self.restrictions = ko.observableArray();
    self.restrictionTypes = ko.observableArray(['Time','Location','Number of Calls']);
    self.selectedRestriction = ko.observable();
    self.countries = ko.observableArray(countries.map(function(element){  return element.name;}));
    self.selectedCountry = ko.observable();
    self.selectedUnit = ko.observable();


    self.isView = function(view){
      return view == self.currentView()
    };
    self.signIn = function(){
      var user = new UserModel(self.userName);
      user.getNumbers();
      self.user(user);
      self.getRestrictions();
      self.currentView("logged");
    };
    self.signOut = function(){
      self.user("");
      self.userName("");
      self.currentView("landing");
    };


    self.createRealNumber = function(){
      var number = $('#newNumber').val();
      $.post("http://46.101.25.199:7999/add_real_phone_number/?user_id=" + self.user().id() +"&real_phone_number=" + number ,{},function(data){
        self.user().realNumbers().push(number);
      })
    }

    self.selectNo = function(type,no){
      if(type=='real') self.rNoSelected(no);
      else self.vNoSelected(no);
    };

    self.isNoSelected = function(type,no){
      if(type=='real') return no == self.rNoSelected();
      else return no == self.vNoSelected()
    };



    self.isRestrictionType = function(type){
      return type === self.selectedRestriction();
    };


    self.selectUnit = function(unit){
      self.selectedUnit(unit);
    }

    self.isSelectedUnit = function(unit){
      return unit == self.selectedUnit();
    };


    self.createRestriction = function(){
      var r = new RestrictionModel();
      r.vNumber(self.vNoSelected());
      r.rNumber(self.rNoSelected());
      r.restrictionType(self.selectedRestriction());
      var options = {};
      if(self.selectedRestriction() == "Time"){
        options.start = $('#start').val();
        options.end = $('#end').val();
        options.weekdays = $('#weekdays').is(':checked');
        options.weekends = $('#weekends').is(':checked');
      }
      else if(self.selectedRestriction() == "Location"){
        options.country = self.selectedCountry();
      }else if(self.selectedRestriction() == "Number of Calls"){
        options.numberCalls = $('#noCalls').val();
        options.numberUnits = $('#noUnits').val();
        options.unit = self.selectedUnit();
      }
      r.restrictionOptions(options);
      var req = {type: r.restrictionType(),
                 options: options,
                 vNumber: self.vNoSelected(),
                 rNumber: self.rNoSelected()};
      $.post("http://46.101.25.199:7999/add_link_with_restrictions/?user_id="
              + self.user().id(), JSON.stringify(req),
              function(data){
                 self.restrictions.push(r);
              });
    }

    self.getRestrictions = function(){
      if(self.user()){
        $.getJSON("http://46.101.25.199:7999/get_links/?user_id=" +
                    self.user().id(),
                    function(data){
                      data.forEach(function(el){
                        var r = new RestrictionModel();
                        r.rNumber(el.rNumber);
                        r.vNumber(el.vNumber);
                        if( el.restriction.type == "NumberCalls") el.restriction.type = "Number of Calls";
                        r.restrictionType(el.restriction.type);
                        r.restrictionOptions(el.restriction.options);
                        self.restrictions.push(r);
                      });
                    });
      }
    }


    self.userName("Joaquim");
    self.signIn();
};

ko.applyBindings(new MenuModel());
