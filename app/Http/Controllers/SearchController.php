<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Interprise;

class SearchController extends Controller
{
    public function index($query)
    {

        $query = trim(preg_replace('!\s+!', ' ', mb_strtolower($query)));
        if (!$query && $query == '') return response('', 400);

        $data = Interprise::where('name_ru','like', '%'.$query.'%')
            ->orWhere('name_kk','like',  '%'.$query.'%')
            ->orWhere('BIN','like',  '%'.$query.'%')
            ->orWhere('register_date','like',  '%'.$query.'%')
            ->orWhere('economic_activity_code','like',  '%'.$query.'%')
            ->orWhere('economic_activity_codes','like',  '%'.$query.'%')
            ->orWhere('company_size_code','like',  '%'.$query.'%')
            ->orWhere('territory_code','like',  '%'.$query.'%')
            ->orWhere('address','like',  '%'.$query.'%')
            ->orWhere('CEO','like',  '%'.$query.'%')
            ->orWhere('active','like',  '%'.$query.'%')
            ->orWhere('resident','like',  '%'.$query.'%')->paginate(30);
        return $data;
    }
}
