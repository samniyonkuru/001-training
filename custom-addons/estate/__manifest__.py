{
    "name": "Real Estate",
    "author": "Samuel",
    "summary": "Test module",
    "version": "19.0.1.0.0",
    "license": "LGPL-3",

    "depends": [
        "crm",
    ],

    "data": [
            # SECURITY
            "security/res_groups.xml",
            "security/ir.model.access.csv",
            # VIEWS
            "views/estate_property_views.xml",
            # MENUS
            "views/estate_menus.xml",
        ],
    "demo": [
            "demo/demo.xml",
        ],
    "application": True,
    "installable": True,
}
