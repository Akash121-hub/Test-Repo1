var person = {
    firstname = "akash",
    lastname = "shinde",
    id = 56,
    fullname = function(){
        return this.firstname + this.lastname
    }
};

name = person.fullname();