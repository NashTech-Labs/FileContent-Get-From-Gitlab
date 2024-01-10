import gitlab
import base64
gitlab_url = "https://gitlab.com"
access_token = <private-token-of-gitlab-project>
gl = gitlab.Gitlab(gitlab_url, private_token=access_token)
gl.auth()
project_id = <project-id>
project = gl.projects.get(project_id)
branch = <branch-name>
try:
    f = project.files.get(file_path=<file-path>, ref=branch)
except gitlab.exceptions.GitlabGetError:
    print("Error: Unable to retrieve file.")
    exit()
file_content = base64.b64decode(f.content).decode("utf-8")
print(file_content)
