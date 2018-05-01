<?php

namespace App\Http\Controllers;

use App\Filial;
use Illuminate\Http\Request;
use App\BadInterprise;
use App\Interprise;
use App\BankrotInterprise;
use App\ExbankrotInterprise;
use App\Branch;
use App\GoodInterprise;
use App\LieInterprise;
use App\TerrorInterprise;
use App\OldBranch;
use App\OldInterprise;
use App\kato;
use App\oked;
use App\Promiser;
use App\Jur;
use App\Codex;

class CompanyController extends Controller
{
    public function index($bin)
    {
        $query_interprise = Interprise::where('BIN', '=', $bin)->first();

        $data['company'] = $query_interprise;
        $data['bad'] = BadInterprise::where('bin', 'like', '%' . substr($query_interprise->BIN, 1, 11) . '%')->get()->count();
        $data['good'] = GoodInterprise::where('bin', 'like', '%' . substr($query_interprise->BIN, 1, 11) . '%')->get()->count();
        $data['bankrot'] = BankrotInterprise::where('bin_iin', 'like', '%' . substr($query_interprise->BIN, 1, 11) . '%')->count();
        $data['exbankrot'] = ExbankrotInterprise::where('bin_iin', 'like', '%' . substr($query_interprise->BIN, 1, 11) . '%')->count();
        $data['lie'] = LieInterprise::where('iin_bin', 'like', '%' . substr($query_interprise->BIN, 1, 11) . '%')->count();
        $data['branch'] = Branch::where('head_BIN', 'like', '%' . substr($query_interprise->BIN, 1, 11) . '%')->count();
        $data['promiser'] = Promiser::where('BIN', 'like', '%' . substr($query_interprise->BIN, 1, 11) . '%')->count();
        $data['codex'] = Codex::where('BIN', 'like', '%' . substr($query_interprise->BIN, 1, 11) . '%')->count();
        $data['jur'] = Jur::where('BIN', 'like', '%' . substr($query_interprise->BIN, 1, 11) . '%')->count();
        $data['ceo']['terror'] = TerrorInterprise::where('name', 'like', '%' . $query_interprise->CEO . '%')->count();
        $data['ceo']['interprises'] = Interprise::where('CEO', 'like', '%' . $query_interprise->CEO . '%')->get();
        $data['ceo']['promiser'] = Promiser::where('CEO', 'like', '%' . $query_interprise->CEO . '%')->get();

        return $data;
    }

    public function getKato($kato){
        $data = kato::where('kato', 'like', '%' .$kato. '%')->get();
        return $data;
    }

    public function getOked($oked){
        $data = oked::where('code', 'like', '%' .$oked. '%')->get();
        return $data;
    }

    public function getFilials($bin){
        $query_interprise = Interprise::where('BIN', '=', $bin)->first();
        preg_match("#'([^']+)'#i", $query_interprise->name_ru, $out);
        $company_name = $out[1];

        $filials = Filial::where('name', 'like', '%' .$company_name .'%')->where('BIN', '<>', $bin)->pluck('name', 'BIN');

        $data = [];
        $i = 0;
        foreach ($filials as $key => $value) {
            $data[$i]['BIN'] = $key;
            $data[$i]['name'] = $value;
            $i++;
        }

        return $data;
    }

    public function getHead($bin){
        $query_interprise = Interprise::where('BIN', '=', $bin)->first();
        preg_match("#'([^']+)'#i", $query_interprise->name_ru, $out);
        $company_name = $out[1];

        $likes = Interprise::where('name_ru', 'like', '%' .$company_name .'%')->where('BIN', '<>', $bin)->pluck('name_ru', 'BIN');

        $data = [];
        foreach ($likes as $key => $value) {
            if(strval($key)[5] == 0){
                $data['BIN'] = $key;
                $data['name'] = $value;
            }
        }
        return $data;
    }

    public function wanted($bin){
        $query_interprise = Interprise::where('BIN', '=', $bin)->first();
        $wanted_query = file_get_contents('http://kgd.gov.kz/ru/wanted?title=&domain=1&name='.$query_interprise->CEO.'&op=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA');
        \phpQuery::newDocument($wanted_query);

        $result = pq('.wanted_body')->html();

        if($result == ""){
            $wanted = 'false';
        } else {
            $wanted = 'true';
        }
        \phpQuery::unloadDocuments();
        return $wanted;
    }
}
