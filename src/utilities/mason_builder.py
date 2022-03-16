MASON_TYPE = "application/vnd.mason+json"



class MasonBuilder(dict):
    def add_error(self, title, details, **kwargs):
        self["@error"] = {
            "@message": title,
            "@messages": [details],
        }
        self['@error'] = kwargs

        return self

    def add_namespace(self, ns, uri):
        if "@namespaces" not in self:
            self["@namespaces"] = {}

        self["@namespaces"][ns] = {
            "name": uri
        }

        return self

    def add_control(self, ctrl_name, href, **kwargs):
        if "@controls" not in self:
            self["@controls"] = {}

        self["@controls"][ctrl_name] = kwargs
        self["@controls"][ctrl_name]["href"] = href

        return self


    def add_control_post(s, ctrl_name, href, **kwargs):
        return s.add_control(
            ctrl_name,
            href,
            method="POST",
            encoding="json",
            title='Creates a new item of interest.',
            **kwargs
        )


    def add_control_put(s, ctrl_name, href, **kwargs):
        return s.add_control(
            ctrl_name,
            href,
            method="PUT",
            encoding="json",
            title='Updtates the item of interest.',
            **kwargs
        )

    def add_control_delete(s, ctrl_name, href, **kwargs):
        return s.add_control(
            ctrl_name,
            href,
            method="DELETE",
            title="Deletes the item of interest.",
            **kwargs
        )
