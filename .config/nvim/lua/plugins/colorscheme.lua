return {
	{
		{
			"Mofiqul/dracula.nvim",
			name = "dracula",
			priority = 1000,
			opts = {
				transparent_bg = true,
			},
		},
		{
			"Gentleman-Programming/gentleman-kanagawa-blur",
			name = "gentleman-kanagawa-blur",
			priority = 1000,
			opts = {
				highlight_overrides = {
					["@variable.python"] = { fg = "#ABB2BF" },
				},
			},
		},
		{
			"LazyVim/LazyVim",
			opts = {
				colorscheme = "gentleman-kanagawa-blur",
			},
		},
	},
}
