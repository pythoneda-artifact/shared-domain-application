# vim: set fileencoding=utf-8
"""
pythoneda/artifact/shared/application/artifact_app.py

This file defines the ArtifactApp class.

Copyright (C) 2023-today rydnr's pythoneda-shared-pythonlang-artf/application

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import asyncio
from pythoneda.shared.artifact import LocalArtifact
from pythoneda.shared.artifact.application import LocalArtifactApp
from pythoneda.artifact.shared.infrastructure import LocalDomainArtifact


class ArtifactApp(LocalArtifactApp):
    """
    Runs the Artifact PythonEDA realm.

    Class name: ArtifactApp

    Responsibilities:
        - Runs the application for pythoneda-shared/domain artifact.

    Collaborators:
        - Command-line handlers from pythoneda-shared-pythonlang-artf/infrastructure
    """

    def __init__(self):
        """
        Creates a new ArtifactApp instance.
        """
        # artifact is automatically generated by pythoneda-shared-pythonlang-artf-def/application's flake
        try:
            from pythoneda.artifact.shared.application.artifact_app_banner import (
                ArtifactAppBanner,
            )

            banner = ArtifactAppBanner()
        except ImportError:
            banner = None

        super().__init__(banner, __file__)

    @classmethod
    def local_artifact_class(cls) -> type[LocalArtifact]:
        """
        Retrieves the subclass of LocalArtifact.
        :return: Such class.
        :rtype: type[LocalArtifact]
        """
        return LocalDomainArtifact


if __name__ == "__main__":
    asyncio.run(ArtifactApp.main("pythoneda.artifact.shared.application.ArtifactApp"))
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End: