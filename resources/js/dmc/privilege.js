var SUPER_ADMINISTRATOR = "0",
    ADMINISTRATOR = "1",
    SUPER_SERVICE_OWNER = "2",
    SERVICE_OWNER = "3",
    SUPER_SITE_OWNER = "4",
    SITE_OWNER = "5",
    VISITOR = "6",
    OCP_OWNER = "7";

/**
 *
 * filter user available actions by user roles
 *
 * @param actions all available actions in page, object array [{},{},{}]
 * @param userRoles user roles, object {}
 * @param privileges privileges at least one of them is needed to preform those actions, string array ["","",""]
 * @param resources resources which actions will be performed on, string array ["","",""]
 * @returns {*} user available actions after filtering via user role
 */
function userActionPrivilegeFilter(actions, userRoles, privileges, resources) {
    var userActions = [];
    if (!actions || actions.length == 0) {
        return userActions;
    }

    if (!privileges || privileges.length == 0) {
        return actions
    }

    var deny = checkPrivilegeAndResource(privileges, resources, userRoles);
    if (deny) {
        return userActions;
    }

    for (var n in actions) {
        if (typeof actions[n] == "object") {
            deny = checkRolesInAction(actions[n], resources, userRoles)
        } else {
            deny = false;
        }
        if (!deny) {
            userActions.push(actions[n]);
        }
    }
    return userActions;
}

function checkRolesInAction(action, resources, userRoles) {
    var actionRole = action["role"];
    if (actionRole && actionRole.length > 0) {
        for (var m in actionRole) {
            var userResources = userRoles[actionRole[m]]
            if (userResources != undefined) {
                if (userResources.length > 0 && resources && resources.length > 0) {
                    var arr = userResources.split(",");
                    for (var j in arr) {
                        for (var k in resources) {
                            if (arr[j] == resources[k]) {
                                return false;
                            }
                        }
                    }
                } else {
                    return false;
                }
            }
        }
        return true;
    } else {
        return false;
    }
}

function checkPrivilegeAndResource(privileges, resources, userRoles) {
    for (var i in privileges) {
        var userResources = userRoles[privileges[i]];
        if (userResources != undefined) {
            if (userResources.length > 0 && resources && resources.length > 0) {
                var arr = userResources.split(",");
                for (var j in arr) {
                    for (var k in resources) {
                        if (arr[j] == resources[k]) {
                            return false;
                        }
                    }
                }
            } else {
                return false;
            }
        }
    }
    return true;
}