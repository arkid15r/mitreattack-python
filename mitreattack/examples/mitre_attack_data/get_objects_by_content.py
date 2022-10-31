from mitreattack.stix20 import MitreAttackData

def main():
    mitre_attack_data = MitreAttackData("path/to/enterprise-attack.json")

    techniques = mitre_attack_data.get_objects_by_content('LSASS', 'technique', remove_revoked_deprecated=True)
    print(f"There are {len(techniques)} techniques where 'LSASS' appears in the description.")

if __name__ == "__main__":
    main()
