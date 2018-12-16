from powerline_shell.themes.default import DefaultColor

white = 255
black = 0
font_color = 232
green = 86
blue = 153
dark_blue = 31
yellow = 230
red = 198
orange = 214

class Color(DefaultColor):
    USERNAME_FG = font_color
    USERNAME_BG = 255
    USERNAME_ROOT_BG = 205

    HOSTNAME_FG = font_color
    HOSTNAME_BG = 230

    HOME_SPECIAL_DISPLAY = False
    PATH_BG = green
    PATH_FG = font_color
    CWD_FG = black
    SEPARATOR_FG = red

    READONLY_BG = 209
    READONLY_FG = 15

    REPO_CLEAN_BG = 150  # pale green
    REPO_CLEAN_FG = 235
    REPO_DIRTY_BG = 203  # pale red
    REPO_DIRTY_FG = 15

    JOBS_FG = 14
    JOBS_BG = font_color

    CMD_PASSED_BG = blue
    CMD_PASSED_FG = font_color
    CMD_FAILED_BG = 198
    CMD_FAILED_FG = 231

    SVN_CHANGES_BG = REPO_DIRTY_BG
    SVN_CHANGES_FG = REPO_DIRTY_FG

    VIRTUAL_ENV_BG = 150
    VIRTUAL_ENV_FG = 0

    AWS_PROFILE_FG = 0
    AWS_PROFILE_BG = 7

    TIME_FG = font_color
    TIME_BG = yellow



    GIT_AHEAD_BG = 240
    GIT_AHEAD_FG = font_color
    GIT_BEHIND_BG = 240
    GIT_BEHIND_FG = font_color
    GIT_STAGED_BG = 194
    GIT_STAGED_FG = font_color
    GIT_NOTSTAGED_BG = 222
    GIT_NOTSTAGED_FG = font_color
    GIT_UNTRACKED_BG = 222
    GIT_UNTRACKED_FG = black
    GIT_CONFLICTED_BG = 9
    GIT_CONFLICTED_FG = font_color

    REPO_CLEAN_BG = 60 
    REPO_CLEAN_FG = 195 
    REPO_DIRTY_BG = 60
    REPO_DIRTY_FG = 195

    GIT_STASH_BG = 221
    GIT_STASH_FG = 0