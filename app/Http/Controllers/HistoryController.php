<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\History;

class HistoryController extends Controller
{
    public function index($bin){
        $company_history = History::where('BIN', '=', $bin)->get();
//        $company_history = History::where('BIN', '=', $bin)->groupBy('update_date')->get();
        return $company_history;
    }
}
