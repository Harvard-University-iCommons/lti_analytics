# LTI Analytics

Easily add user interaction data collection to your LTI tools.

## Django Apps

### Interactions

#### Installation

1. Run `pip install git+ssh://git@github.com/Harvard-University-iCommons/lti_analytics.git@develop#egg=lti_analytics==develop`

2. Add `interactions` to INSTALLED_APPS.

3. Add `{% include 'interactions/interactions.html' %}` to templates from which you would like to collect interaction data.

#### Usage

To record interaction data you can pass a Javascript object containing the data you would like to record to `LTIAnalytics.pushInteraction()`:

    LTIAnalytics.pushInteraction({action: 'click', entity: 'my_awesome_button'});

LTI session parameters will also be stored with each interaction.
