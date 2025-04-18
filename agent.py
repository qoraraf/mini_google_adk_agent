# astro_agent/agent.py
"""
Minimal ADK agent that answers beginner astronomy questions.
It demonstrates:
  • Multiple function tools
  • Simple error handling
  • Gemini model selection by string ID
"""

from typing import Dict

# ADK imports
from google.adk.agents import Agent           



# ---------- TOOL 1: planet_fact ----------
def planet_fact(planet: str) -> Dict[str, str]:
    """Return a fun fact about a Solar‑System planet."""
    facts = {
        "Mercury": "Mercury orbits the Sun in just 88 Earth‑days.",
        "Venus":   "Venus rotates backwards (retrograde spin).",
        "Earth":   "Earth is the densest planet in the Solar System.",
        "Mars":    "Mars hosts the tallest known volcano, Olympus Mons.",
        "Jupiter": "Jupiter has a persistent anticyclonic storm called the Great Red Spot.",
        "Saturn":  "Saturn’s rings are less than 1 km thick in most places.",
        "Uranus":  "Uranus spins on its side—its axial tilt is 98°.",
        "Neptune": "Neptune was the first planet found by mathematical prediction."
    }
    fact = facts.get(planet.title())
    if fact:
        return {"status": "success", "fact": fact}
    return {
        "status": "error",
        "error_message": f"Sorry, I don’t have a fact for '{planet}'."
    }

# ---------- TOOL 2: days_in_year ----------
def days_in_year(planet: str) -> Dict[str, str]:
    """Return the orbital period (planetary year) in Earth days."""
    periods = {
        "Mercury": 88,
        "Venus":   225,
        "Earth":   365.25,
        "Mars":    687,
        "Jupiter": 4333,
        "Saturn":  10759,
        "Uranus":  30687,
        "Neptune": 60190
    }
    days = periods.get(planet.title())
    if days:
        return {
            "status": "success",
            "report": f"One {planet.title()} year ≈ {days:,} Earth days."
        }
    return {
        "status": "error",
        "error_message": f"Unknown planet '{planet}'."
    }

# ---------- ROOT AGENT ----------
root_agent = Agent(
    name="mini_astro_tutor",
    model="gemini-2.0-flash", 
    description="An agent that teaches basic Solar‑System facts.",
    instruction=(
        "You are a friendly astronomy tutor. "
        "When the user asks about a planet, decide whether to call:\n"
        "  • planet_fact for a general fun fact\n"
        "  • days_in_year if they ask about orbital period or length of the year\n"
        "If no tool is appropriate, answer directly."
    ),
    tools=[planet_fact, days_in_year],
)