from re import compile


def _class_content_str_to_list(class_content: str):
    result = {}
    for content in class_content.strip().split("\n"):
        content_filter = content.strip()
        if content_filter:
            attribute, content = content_filter.split(":")
            result.update({attribute: content.strip().split(";")[0]})
    return result


def _class_css_to_python_dict(css_code: str):
    pattern = compile(r"\.(\w[\w\-]*)\s*\{([^}]*)\}")
    matches = pattern.findall(css_code)

    result = {}

    for match in matches:
        class_name, class_content = match
        class_content_list = _class_content_str_to_list(class_content)
        result[f".{class_name}"] = class_content_list

    return result


# def _get_class_content_from_css(css_code: str):
#     result = _class_css_to_python_dict(css_code)
#     print(result)


def get_app_style_from_css(path: str):
    with open(path, "r") as f:
        data = f.read()
        style = _class_css_to_python_dict(data)
        return style
