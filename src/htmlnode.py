class HTMLNode:
    def __init__(self, tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_props = ""
        keys = list(self.props.keys())
        last_index = len(keys) - 1

        for index, key in enumerate(keys):
           value = self.props[key]
           html_props += f'{key}="{value}"'
           if index != last_index:
               html_props += ' '
            
        return html_props
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return NotImplemented
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

    
