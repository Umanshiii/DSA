class Solution:
    def simplifyPath(self, path: str) -> str:
        segments = path.split('/')
        path_stack = []
        
        for segment in segments:
            if segment in ("", "."):
                continue
            
            if segment == "..":
                if path_stack:
                    path_stack.pop()
            else:
                path_stack.append(segment)

        return "/" + "/".join(path_stack)