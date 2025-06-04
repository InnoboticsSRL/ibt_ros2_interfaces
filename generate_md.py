import os

def parse_fields(lines):
    description_lines = []
    fields = []

    in_description = True

    for line in lines:
        line = line.strip()
        if not line:
            if in_description:
                description_lines.append('')
            continue

        if line.startswith('#'):
            comment_text = line[1:].strip()
            if in_description:
                description_lines.append(comment_text)
            continue

        in_description = False

        parts = line.split('#', 1)
        main_part = parts[0].strip()
        inline_comment = parts[1].strip() if len(parts) > 1 else ''

        # Skip enums (lines with '=')
        if '=' in main_part:
            continue

        tokens = main_part.split()
        if len(tokens) >= 2:
            field_type = tokens[0]
            field_name = tokens[1]
            fields.append((field_type, field_name, inline_comment))
        else:
            print(f"⚠️ Skipped invalid line: '{line}'")

    description = '\n'.join(description_lines).strip()
    return description, fields

def parse_msg_file(path, rel_path):
    try:
        with open(path, 'r') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"❌ Error reading {rel_path}: {e}")
        return [f"### `{rel_path}` (Error reading file)", ""]

    description, fields = parse_fields(lines)
    out = [f"### `{rel_path}`", ""]

    if description:
        out.append(description)
        out.append("")

    for t, n, c in fields:
        out.append(f"- `{t} {n}`" + (f": {c}" if c else ""))
    out.append("")
    return out

def parse_srv_file(path, rel_path):
    try:
        with open(path, 'r') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading {rel_path}: {e}")
        return [f"### `{rel_path}` (Error reading file)", ""]

    if '---' not in content:
        print(f"⚠️ File {rel_path} is missing the '---' separator")
        return [f"### `{rel_path}` (Invalid service format)", ""]

    req, resp = content.split('---', 1)

    out = [f"### `{rel_path}`", ""]

    # Request
    out.append("**Request**")
    description, fields = parse_fields(req.strip().splitlines())
    if description:
        out.append(description)
        out.append("")
    for t, n, c in fields:
        out.append(f"- `{t} {n}`" + (f": {c}" if c else ""))
    out.append("")

    # Response
    out.append("**Response**")
    description, fields = parse_fields(resp.strip().splitlines())
    if description:
        out.append(description)
        out.append("")
    for t, n, c in fields:
        out.append(f"- `{t} {n}`" + (f": {c}" if c else ""))
    out.append("")

    return out

def parse_action_file(path, rel_path):
    try:
        with open(path, 'r') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading {rel_path}: {e}")
        return [f"### `{rel_path}` (Error reading file)", ""]

    parts = content.split('---')
    if len(parts) != 3:
        print(f"⚠️ File {rel_path} does not have exactly 3 parts separated by '---'")
        return [f"### `{rel_path}` (Invalid action format)", ""]

    goal, result, feedback = parts

    out = [f"### `{rel_path}`", ""]

    # Goal
    out.append("**Goal**")
    description, fields = parse_fields(goal.strip().splitlines())
    if description:
        out.append(description)
        out.append("")
    for t, n, c in fields:
        out.append(f"- `{t} {n}`" + (f": {c}" if c else ""))
    out.append("")

    # Result
    out.append("**Result**")
    description, fields = parse_fields(result.strip().splitlines())
    if description:
        out.append(description)
        out.append("")
    for t, n, c in fields:
        out.append(f"- `{t} {n}`" + (f": {c}" if c else ""))
    out.append("")

    # Feedback
    out.append("**Feedback**")
    description, fields = parse_fields(feedback.strip().splitlines())
    if description:
        out.append(description)
        out.append("")
    for t, n, c in fields:
        out.append(f"- `{t} {n}`" + (f": {c}" if c else ""))
    out.append("")

    return out

def generate_documentation(pkg_path='ibt_ros2_interfaces', output_file='README.md'):
    print(f"ℹ️ Starting scan of package '{pkg_path}'")

    msg_path = 'msg'
    srv_path =  'srv'
    action_path = 'action'

    output = [f"# {pkg_path}", ""]

    if os.path.isdir(msg_path):
        print(f"ℹ️ Found msg directory: {msg_path}")
        output.append("## Messages\n")
        for f in sorted(os.listdir(msg_path)):
            if f.endswith('.msg'):
                rel = f"{pkg_path}/msg/{f}"
                print(f"  📄 Processing {rel}")
                output += parse_msg_file(os.path.join(msg_path, f), rel)
    else:
        print(f"⚠️ Msg directory not found: {msg_path}")

    if os.path.isdir(srv_path):
        print(f"ℹ️ Found srv directory: {srv_path}")
        output.append("## Services\n")
        for f in sorted(os.listdir(srv_path)):
            if f.endswith('.srv'):
                rel = f"{pkg_path}/srv/{f}"
                print(f"  📄 Processing {rel}")
                output += parse_srv_file(os.path.join(srv_path, f), rel)
    else:
        print(f"⚠️ Srv directory not found: {srv_path}")

    if os.path.isdir(action_path):
        print(f"ℹ️ Found action directory: {action_path}")
        output.append("## Actions\n")
        for f in sorted(os.listdir(action_path)):
            if f.endswith('.action'):
                rel = f"{pkg_path}/action/{f}"
                print(f"  📄 Processing {rel}")
                output += parse_action_file(os.path.join(action_path, f), rel)
    else:
        print(f"⚠️ Action directory not found: {action_path}")

    with open(output_file, 'w') as f:
        f.write('\n'.join(output))

    print(f"✅ File `{output_file}` generated successfully.")

if __name__ == "__main__":
    generate_documentation()
