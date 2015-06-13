var RestrictionModel = function() {
    self = this;
    self.vNumber = ko.observable();
    self.rNumber = ko.observable();
    self.restrictionType = ko.observable();
    self.restrictionOptions = ko.observable();

    self.printRestriction = function(){
      var options = self.restrictionOptions();
      if(self.restrictionType() == "Time"){
        var postRet = "";
        if(options.weekdays && options.weekends){
          postRet = ".";
        }else if(options.weekdays && !options.weekends){
          postRet = " on weekdays.";
        }else if(!options.weekdays && options.weekends){
          postRet = " on weekends.";
        }
        if(postRet) return "From " + options.start + " to " + options.end + postRet;
        else return "Never";
      }
      else if(self.restrictionType() == "Location"){
        return "Only if in " + options.country + ".";
      }else if(self.restrictionType() == "Number of Calls"){
        return "Only " + options.numberCalls + " calls within " +
                options.numberUnits + " " + options.unit + ".";
      }

    }
};
