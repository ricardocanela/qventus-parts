from parts.models import Part

def run():
    if Part.objects.exists():
        return

    Part.objects.create(
        name="Heavy coil",
        sku="SDJDDH8223DHJ",
        description="Tightly wound nickel-gravy alloy spring",
        weight_ounces=22,
        is_active=True
    )
    Part.objects.create(
        name="Reverse lever",
        sku="DCMM39823DSJD",
        description="Attached to provide inverse leverage",
        weight_ounces=9,
        is_active=False
    )
    Part.objects.create(
        name="Macrochip",
        sku="OWDD823011DJSD",
        description="Used for heavy-load computing",
        weight_ounces=2,
        is_active=True
    )

    print("✅ Sample data inserted.")

run()
