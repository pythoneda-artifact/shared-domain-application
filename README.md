# Domain Artifact Application

Application layer for [pythoneda-shared-pythoneda](https://github.com/pythoneda-shared-pythoneda "pythoneda-shared-pythoneda")/[domain-artifact](https://github.com/pythoneda-shared-pythoneda/domain-artifact "domain-artifact").

## How to declare it in your flake

Check the latest tag of the artifact repository: [https://github.com/pythoneda-shared-pythoneda/domain-artifact-application-artifact/tags](https://github.com/pythoneda-shared-pythoneda/domain-artifact-application-artifact/tags) and use it instead of the `[version]` placeholder below.

```nix
{
  description = "[..]";
  inputs = rec {
    [..]
    pythoneda-shared-pythoneda-domain-artifact-application = {
      [optional follows]
      url =
        "github:pythoneda-shared-pythoneda/domain-artifact-application/[version]?dir=domain-artifact-application";
    };
  };
  outputs = [..]
};
```

Should you use another PythonEDA modules, you might want to pin those also used by this project. The same applies to [nixpkgs](https://github.com/nixos/nixpkgs "nixpkgs") and [flake-utils](https://github.com/numtide/flake-utils "flake-utils").

Use the specific package depending on your system (one of `flake-utils.lib.defaultSystems`) and Python version:

- `#packages.[system].pythoneda-shared-pythoneda-domain-artifact-application-python38` 
- `#packages.[system].pythoneda-shared-pythoneda-domain-artifact-application-python39` 
- `#packages.[system].pythoneda-shared-pythoneda-domain-artifact-application-python310` 
- `#packages.[system].pythoneda-shared-pythoneda-domain-artifact-application-python311` 

The Nix flake is under the 
[domain-artifact-application](https://github.com/pythoneda-shared-pythoneda/domain-artifact-application-artifact/tree/main/domain-artifact-application "domain-artifact-application") folder.
