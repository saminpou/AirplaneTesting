import * as users from 'users';

class Group{
    constructor(name, parent) {
        this.name = name;
        this.parent = parent;
    }
}
class Groups{
    constructor() {
        this.group_names = {};
    }
    add(name, parent_name) {
        var new_group, parent_group;
        if (parent_name === null) {
            new_group = new Group(name, null);
        } else if (!parent_name in self.group_names) {
                console.log("Error finding parent");
        } else {
            parent_group = this.group_names[parent_name];
            new_group = new Group(name, parent_group);
        }
    }
    get(name) {
        if (!name in self.group_names) {
            console.log("Error finding group");
        } else {
            return this.group_names[name];
        }
    }
}

//# sourceMappingURL=groups.js.map
