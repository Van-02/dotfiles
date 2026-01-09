local opt = vim.opt

-- Line numbers
opt.number = true   	
opt.relativenumber = true

-- Tabs
opt.tabstop = 4		    	-- Un tabulador equivale a 4 espacios
opt.softtabstop = 4
opt.shiftwidth = 4	    	-- Tamaño de la sangrua automatica
opt.expandtab = true	    	-- Convertir tabs en espacios

-- Indentation
opt.smartindent = true

-- Don't wrap text
opt.wrap = false

-- Searching
opt.hlsearch = false
opt.incsearch = true
opt.ignorecase = true       	-- Ignorar mayúsculas al buscar
opt.smartcase = true        	-- Si buscas con una mayúscula, se vuelve sensible

-- Colors
opt.termguicolors = true    	-- Colores reales (necesario para temas modernos)

-- Vertical markers
opt.signcolumn = 'yes'
opt.colorcolumn = '80'

opt.mouse = 'a'             	-- Habilitar ratón
opt.clipboard = 'unnamedplus'	-- Usa el portapapeles del sistema 
