<?php

namespace App\Http\Controllers;

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

class CompanyController extends Controller
{
    public function index($id)
    {
        $query_interprise = Interprise::find($id);

        $data['company'] = $query_interprise;
        $data['old'] = OldInterprise::where('BIN', 'like', '%' . substr($query_interprise->BIN, 1, 11) . '%')->get();
        $data['bad'] = BadInterprise::where('bin', 'like', '%' . substr($query_interprise->BIN, 1, 11) . '%')->get()->count();
        $data['good'] = GoodInterprise::where('bin', 'like', '%' . substr($query_interprise->BIN, 1, 11) . '%')->get()->count();
        $data['bankrot'] = BankrotInterprise::where('bin_iin', 'like', '%' . substr($query_interprise->BIN, 1, 11) . '%')->count();
        $data['exbankrot'] = ExbankrotInterprise::where('bin_iin', 'like', '%' . substr($query_interprise->BIN, 1, 11) . '%')->count();
        $data['lie'] = LieInterprise::where('iin_bin', 'like', '%' . substr($query_interprise->BIN, 1, 11) . '%')->count();
        $data['OldBranch'] = OldBranch::where('head_BIN', 'like', '%' . substr($query_interprise->BIN, 1, 11) . '%')->count();
        $data['branch'] = Branch::where('head_BIN', 'like', '%' . substr($query_interprise->BIN, 1, 11) . '%')->count();

        $data['ceo']['terror'] = TerrorInterprise::where('name', 'like', '%' . $query_interprise->CEO . '%')->count();

        return $data;
    }
}
