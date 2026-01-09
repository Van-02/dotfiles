vim.g.mapleader = " "
-- Map Ctrl+c to escape from other modes
vim.keymap.set({ "i", "n", "v" }, "<C-c>", [[<C-\><C-n>]])

-- Redefine Ctrl+s to save with the custom function

-- Delete all buffers but the current one
vim.keymap.set("n","<leader>bq",'<Esc>:%bdelete|edit #|normal`"<Return>', { desc = "Delete other buffers but the current one" })

-- Screen Keys
vim.keymap.set({ "n" }, "<leader>uk", "<cmd>Screenkey<CR>")

-- Custom save function
function SaveFile()
    -- Verificar si el buffer tiene un nombre de archivo
    if vim.fn.empty(vim.fn.expand("%:t")) == 1 then
        vim.notify("No hay archivo para guardar", vim.log.levels.WARN)
        return
    end

    local filename = vim.fn.expand("%:t")
    local success, err = pcall(function()
        vim.cmd("silent! write")
    end)

    if success then
        -- Las notificaciones elegantes que usa Gentleman
        vim.notify(filename .. " Guardado!", vim.log.levels.INFO)
    else
        vim.notify("Error al guardar: " .. err, vim.log.levels.ERROR)
    end
end

vim.keymap.set("n", "<C-s>", SaveFile(), { noremap = true, silent = true })
