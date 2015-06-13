var MenuModel = function() {
    var self = this;

    self.user = ko.observable("default");
    self.userName = ko.observable();

    self.currentView = ko.observable("landing");


    self.restrictions = ko.observableArray(['Time','Location','Number of Calls']);
    self.selectedRestriction = ko.observable();
    self.countries = ko.observableArray(countries.map(function(element){  return element.name;}));
    self.selectedCountry = ko.observable();


    self.isView = function(view){
      return view == self.currentView()
    };
    self.signIn = function(){
      var user = new UserModel(self.userName);
      user.getNumbers();
      self.user(user);
      self.currentView("logged");
    };
    self.signOut = function(){
      self.user("");
      self.userName("");
      self.currentView("landing");
    };
    self.isRestrictionType = function(type){
      return type === self.selectedRestriction();
    }

    self.userName("José");
    self.signIn();
};

ko.applyBindings(new MenuModel());
