var UserModel = function() {
    self = this;
    self.username = ko.observable();
    self.realNumbers = ko.observableArray();
    self.virtualNumbers = ko.observableArray();
    this.getNumbers = function() {
        self.realNumbers(['913451234','931236578','963456857']);
        self.virtualNumbers(['342623465', '325476980', '304568293']);
    } // Ensure that "this" is always this view model
};
