" Author: Philip <philipkarlsson@me.com>
" Description: Main entry point for the plugin: sets up prefs and autocommands
"   Preferences can be set in vimrc files and so on to configure aerojump

" Tbd, below is just an example
nnoremap <silent> <Plug>(R2Rax) :R2 rax<Return>

function TestMe(inp_str)
    let buf = nvim_create_buf(v:false, v:true)
    call nvim_buf_set_lines(buf, 0, -1, v:true, a:inp_str)
    let opts = {'relative': 'cursor', 'width': 20, 'height': 40, 'col': 0,
        \ 'row': 1, 'anchor': 'NW', 'style': 'minimal'}
    let win = nvim_open_win(buf, 0, opts)
    " optional: change highlight, otherwise Pmenu is used
    call nvim_win_set_option(win, 'winhl', 'Normal:MyHighlight')
endfunction
