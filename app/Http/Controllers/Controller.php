<?php

namespace App\Http\Controllers;

use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Routing\Controller as BaseController;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Foundation\Auth\Access\AuthorizesRequests;

class Controller extends BaseController
{
    use AuthorizesRequests, DispatchesJobs, ValidatesRequests;

    public function getToken(){
        return csrf_field();
    }

    public function getAuthStatus(){
        if(auth()->guard()->guest()){
            return 'guest';
        } else {
            return 'auth';
        }
    }
}
