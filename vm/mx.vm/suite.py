suite = {
    "name": "vm",
    "version" : "1.0.0-rc14",
    "release" : True,
    "groupId" : "org.graalvm",
    "mxversion": "5.210.2",
    "defaultLicense" : "GPLv2-CPE",
    "imports": {
        "suites": [
            {
                "name": "truffle",
                "subdir": True,
                "urls": [
                    {"url": "https://curio.ssw.jku.at/nexus/content/repositories/snapshots", "kind": "binary"},
                ]
            },
            # Dynamic imports for components:
            {
                "name": "graal-nodejs",
                "subdir": True,
                "dynamic": True,
                "version": "301d8804261c2326097a25543ecd0ca98ccf74ab",
                "urls" : [
                    {"url" : "https://github.com/graalvm/graaljs.git", "kind" : "git"},
                    {"url": "https://curio.ssw.jku.at/nexus/content/repositories/snapshots", "kind": "binary"},
                ]
            },
            {
                "name": "graal-js",
                "subdir": True,
                "dynamic": True,
                "version": "301d8804261c2326097a25543ecd0ca98ccf74ab",
                "urls": [
                    {"url": "https://github.com/graalvm/graaljs.git", "kind" : "git"},
                    {"url": "https://curio.ssw.jku.at/nexus/content/repositories/snapshots", "kind": "binary"},
                ]
            },
            {
                "name": "truffleruby",
                "version": "ed796f79515351f8c569306e01775c13e48876e8",
                "dynamic": True,
                "urls": [
                    {"url": "https://github.com/oracle/truffleruby.git", "kind": "git"},
                    {"url": "https://curio.ssw.jku.at/nexus/content/repositories/snapshots", "kind": "binary"},
                ],
                "os_arch": {
                    "linux": {
                        "sparcv9": {
                            "ignore": True
                        },
                        "<others>": {
                            "ignore": False
                        }
                    },
                    "<others>": {
                        "<others>": {
                            "ignore": False
                        }
                    }
                }
            },
            {
                "name": "fastr",
                "version": "747947696b5aa8c1cac347b27fb36d0688723f3a",
                "dynamic": True,
                "urls": [
                    {"url": "https://github.com/oracle/fastr.git", "kind": "git"},
                    {"url": "https://curio.ssw.jku.at/nexus/content/repositories/snapshots", "kind": "binary"},
                ]
            },
            {
                "name": "graalpython",
                "version": "11b7224110c66dd43fa22c7cafcb882b51a1e588",
                "dynamic": True,
                "urls": [
                    {"url": "https://github.com/graalvm/graalpython.git", "kind": "git"},
                    {"url": "https://curio.ssw.jku.at/nexus/content/repositories/snapshots", "kind": "binary"},
                ]
            },
        ]
    },

    "projects": {
        "com.oracle.graalvm.locator": {
            "subDir": "src",
            "sourceDirs": ["src"],
            "dependencies": [
                "truffle:TRUFFLE_API",
            ],
            "checkstyleVersion" : "8.8",
            "javaCompliance": "1.8",
            "license": "GPLv2-CPE",
        },
        "org.graalvm.component.installer" : {
            "subDir" : "src",
            "sourceDirs" : ["src"],
            "javaCompliance" : "1.8",
            "checkstyle": "com.oracle.graalvm.locator",
            "license" : "GPLv2-CPE",
        },
        "org.graalvm.component.installer.test" : {
            "subDir" : "src",
            "sourceDirs" : ["src"],
            "dependencies": [
                "mx:JUNIT",
                "org.graalvm.component.installer"
            ],
            "javaCompliance" : "1.8",
            "checkstyle": "com.oracle.graalvm.locator",
            "license" : "GPLv2-CPE",
        },
    },

    "distributions": {
        "LOCATOR": {
            "dependencies": ["com.oracle.graalvm.locator"],
            "distDependencies": [
                "truffle:TRUFFLE_API",
            ],
            "maven": False,
        },
        "INSTALLER": {
            "subDir": "src",
            "mainClass": "org.graalvm.component.installer.ComponentInstaller",
            "dependencies": [
                "org.graalvm.component.installer",
            ],
            "maven" : False,
        },
        "INSTALLER_TESTS": {
            "subDir": "src",
            "dependencies": ["org.graalvm.component.installer.test"],
            "exclude": [
                "mx:HAMCREST",
                "mx:JUNIT",
            ],
            "distDependencies": [
                "INSTALLER",
            ],
            "maven": False,
        },
        "INSTALLER_GRAALVM_SUPPORT": {
            "native": True,
            "platformDependent": True,
            "description": "GraalVM Installer support distribution for the GraalVM",
            "layout": {
                "./": [
                    "dependency:vm:INSTALLER",
                ],
                "bin/": "file:mx.vm/gu",
                "components/polyglot/.registry" : "string:",
            },
            "maven": False,
        },
        "VM_GRAALVM_SUPPORT": {
            "native": True,
            "description": "VM support distribution for the GraalVM",
            "layout": {
                "LICENSE": "file:LICENSE_GRAALVM_CE",
                "3rd_party_licenses.txt": "file:3rd_party_licenses_graalvm_ce.txt",
            },
            "maven": False,
        },
    },
}
