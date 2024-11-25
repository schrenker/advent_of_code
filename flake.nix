{
  outputs = inputs@{ self, nixpkgs, flake-parts, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [ "x86_64-linux" "aarch64-darwin" ];
      perSystem = { config, self', inputs', pkgs, ... }: {
        devShells.default = pkgs.mkShell {
          nativeBuildInputs = with pkgs; [ python313 shellcheck ];
          shellHook = ''
            python -m venv .venv
            source .venv/bin/activate
          '';
        };
      };
    };

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";

    flake-parts.url = "github:hercules-ci/flake-parts";

  };
}
