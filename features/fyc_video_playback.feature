@regression @video_playback
Feature: Automate FYC video playback and controls

  Background:
    Given I launch the FYC application

  @smoke
  Scenario: Complete video playback automation
    When I sign in using PIN "WVMVHWBS"
    Then I navigate to "Test Automation Project"
    And I switch to Details tab and wait for few seconds
    And I return to Videos tab
    And I play the video for 10 seconds and pause
    And I resume playback using Continue Watching button
    And I set video volume to 50 percent
    And I change video resolution to 480p and then back to 720p
    And I pause video and exit project
    And I logout from the platform