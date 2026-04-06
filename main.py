import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_key, player_value in players.items():
        race, _ = Race.objects.get_or_create(
            name=player_value.get("race").get("name"),
            description=player_value.get("race").get("description", '')
        )

        skills = player_value.get("race").get("skills")
        for skill in skills:
            skills, _ = Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race)

        guild, _ = Guild.objects.get_or_create(
            name=player_value.get("guild").get("name"),
            description=player_value.get("guild").get("description")
        )

        players, _ = Player.objects.get_or_create(
            nickname=player_key,
            email=player_value.get("email"),
            bio=player_value.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
