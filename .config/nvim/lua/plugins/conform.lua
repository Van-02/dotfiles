return {
	"stevearc/conform.nvim",
	opts = {
		formatters_by_ft = {
			python = { "black" },
		},

		formatters = {
			black = {
				prepend_args = { "--line-lenght", "80" },
			},
		},
	},
}
