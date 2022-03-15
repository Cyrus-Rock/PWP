MASON_TYPE = "application/vnd.mason+json"



class MasonBuilder(dict):
    def add_error(self, title, details, **kwargs):
        self["@error"] = {
            "@message": title,
            "@messages": [details],
        }
        self['@error'] = kwargs

    def add_namespace(self, ns, uri):
        if "@namespaces" not in self:
            self["@namespaces"] = {}

        self["@namespaces"][ns] = {
            "name": uri
        }

    def add_control(self, ctrl_name, href, **kwargs):
        if "@controls" not in self:
            self["@controls"] = {}

        self["@controls"][ctrl_name] = kwargs
        self["@controls"][ctrl_name]["href"] = href


    def add_control_post(s, ctrl_name, href, **kwargs):
        s.add_control(
            ctrl_name,
            href,
            method="POST",
            encoding="json",
            **kwargs
        )
