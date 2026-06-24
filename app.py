from plugin_manager import (
    PluginManager
)

manager = PluginManager()

while True:

    print(
        "\n======================"
    )

    print(
        "PLUGIN STUDIO"
    )

    print(
        "======================"
    )

    print(
        "1. Create Plugin"
    )

    print(
        "2. Run Plugin"
    )

    print(
        "3. Enable Plugin"
    )

    print(
        "4. Disable Plugin"
    )

    print(
        "5. List Plugins"
    )

    print(
        "6. Exit"
    )

    choice = input(
        "\nChoice: "
    )

    if choice == "1":

        name = input(
            "\nPlugin Name: "
        )

        response = input(
            "Plugin Response: "
        )

        manager.create_plugin(

            name,

            response

        )

        print(
            "\nPlugin Created"
        )

    elif choice == "2":

        name = input(
            "\nPlugin Name: "
        )

        print(
            "\nOutput:"
        )

        print(
            manager.run_plugin(
                name
            )
        )

    elif choice == "3":

        name = input(
            "\nPlugin Name: "
        )

        manager.enable_plugin(
            name
        )

        print(
            "\nEnabled"
        )

    elif choice == "4":

        name = input(
            "\nPlugin Name: "
        )

        manager.disable_plugin(
            name
        )

        print(
            "\nDisabled"
        )

    elif choice == "5":

        plugins = (
            manager.list_plugins()
        )

        print(
            "\nInstalled Plugins:\n"
        )

        for name, info in (
            plugins.items()
        ):

            print(
                f"{name} | "
                f"Enabled: "
                f"{info['enabled']}"
            )

    elif choice == "6":

        break