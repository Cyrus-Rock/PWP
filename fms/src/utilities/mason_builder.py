'''
Functionalities that facilitate the use of hypermedia are defined in this file.
'''
MASON_TYPE = "application/vnd.mason+json"



class MasonBuilder(dict):
    """
    A convenience class for managing dictionaries that represent Mason
    objects. It provides nice shorthands for inserting some of the more
    elements into the object but mostly is just a parent for the much more
    useful subclass defined next. This class is generic in the sense that it
    does not contain any application specific implementation details.
    """
    def add_error(self, title, details, **kwargs):
        """
        Adds an error element to the object. Should only be used for the root
        object, and only in error scenarios.

        Note: Mason allows more than one string in the @messages property (it's
        in fact an array). However we are being lazy and supporting just one
        message.

        : param str title: Short title for the error
        : param str details: Longer human-readable description
        """
        self["@error"] = {
            "@message": title,
            "@messages": [details],
        }
        self['@error'] = kwargs

        return self

    def add_namespace(self, ns, uri):
        """
        Adds a namespace element to the object. A namespace defines where our
        link relations are coming from. The URI can be an address where
        developers can find information about our link relations.

        : param str ns: the namespace prefix
        : param str uri: the identifier URI of the namespace
        """
        if "@namespaces" not in self:
            self["@namespaces"] = {}

        self["@namespaces"][ns] = {
            "name": uri
        }

        return self

    def add_control(self, ctrl_name, href, **kwargs):
        """
        Adds a control property to an object. Also adds the @controls property
        if it doesn't exist on the object yet. Technically only certain
        properties are allowed for kwargs but again we're being lazy and don't
        perform any checking.

        The allowed properties can be found from here
        https://github.com/JornWildt/Mason/blob/master/Documentation/Mason-draft-2.md

        : param str ctrl_name: name of the control (including namespace if any)
        : param str href: target URI for the control
        """

        if "@controls" not in self:
            self["@controls"] = {}

        self["@controls"][ctrl_name] = kwargs
        self["@controls"][ctrl_name]["href"] = href

        return self


    def add_control_post(s, ctrl_name, href, **kwargs):
        """
        Utility method for adding POST type controls. The control is
        constructed from the method's parameters. Method and encoding are
        fixed to "POST" and "json" respectively.
        
        : param str ctrl_name: name of the control (including namespace if any)
        : param str href: target URI for the control
        """
        return s.add_control(
            ctrl_name,
            href,
            method="POST",
            encoding="json",
            title='Creates a new item of interest.',
            **kwargs
        )


    def add_control_put(s, ctrl_name, href, **kwargs):
        """
        Utility method for adding PUT type controls. The control is
        constructed from the method's parameters. Method and encoding
        are fixed to "PUT" and "json" respectively.
        
        : param str ctrl_name: name of the control (including namespace if any)
        : param str href: target URI for the control
        """
        return s.add_control(
            ctrl_name,
            href,
            method="PUT",
            encoding="json",
            title='Updtates the item of interest.',
            **kwargs
        )

    def add_control_delete(s, ctrl_name, href, **kwargs):
        """
        Utility method for adding PUT type controls. The control is
        constructed from the method's parameters. Control method is fixed to
        "DELETE".

        : param str ctrl_name: name of the control (including namespace if any)
        : param str href: target URI for the control
        """
        return s.add_control(
            ctrl_name,
            href,
            method="DELETE",
            title="Deletes the item of interest.",
            **kwargs
        )
