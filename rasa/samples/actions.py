from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionRedirectToHelpline(Action):
    def name(self) -> Text:
        return "action_redirect_to_helpline"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Here is the contact information for a helpline: 0800-0113. Please reach out to them for immediate help. They're available anytime with no costs.")
        return []
