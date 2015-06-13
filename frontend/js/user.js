var UserModel = function() {
    self = this;
    self.id = ko.observable(1)
    self.username = ko.observable();
    self.realNumbers = ko.observableArray();
    self.virtualNumbers = ko.observableArray();
    this.getNumbers = function() {
      $.getJSON("http://46.101.25.199:7999/get_real_phone_numbers/?user_id=" + self.id(), function(data) {
        var numbers = data.map(function(el){ return el.number; });
        self.realNumbers(numbers);
      });
      $.getJSON("http://46.101.25.199:7999/get_virtual_phone_numbers/?user_id=" + self.id(), function(data) {
        var numbers = data.map(function(el){ return el.number; });
        self.virtualNumbers(numbers);
      });
        //self.realNumbers(['913451234','931236578','963456857']);
        //self.virtualNumbers(['342623465', '325476980', '304568293']);
    } // Ensure that "this" is always this view model


    self.deleteNumber = function(number){

      $.getJSON("http://46.101.25.199:7999/delete_real_phone_number/?user_id="
          + self.id() +"&real_phone_number=" + number,function(data){
         self.realNumbers().remove(number);
         
      })
    }
};
