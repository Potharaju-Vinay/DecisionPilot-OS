class ToolRegistry:

    def __init__(self):

        self._tools = {}

    def register(
        self,
        name: str,
        tool
    ):

        self._tools[name] = tool

    def get(
        self,
        name: str
    ):

        if name not in self._tools:

            raise ValueError(

                f"Tool '{name}' is not registered."

            )

        return self._tools[name]

    def exists(
        self,
        name: str
    ):

        return name in self._tools

    def list_tools(self):

        return list(
            self._tools.keys()
        )

    def clear(self):

        self._tools.clear()