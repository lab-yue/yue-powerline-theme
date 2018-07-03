config_dir="/Users/${USER}/.config/powerline-shell/";
theme_name="yue";
sed -i '-origin.json' "s/USER/${USER}/g" config.json
cp ${config_dir}config.json ${config_dir}config-origin.json
cp config.json ${config_dir}config.json
cp ${theme_name}.py /Users/$USER/powerline-shell/build/lib/powerline_shell/themes/${theme_name}.py
echo "success"
