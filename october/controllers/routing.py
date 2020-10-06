import datetime
import odoo

from odoo import http
from odoo.http import request

class October(http.Controller):
    # -- Sample routing
    # @http.route('/test', website=True, auth='public')
    # def test_route(self, **kw):
    #    return request.render("october.test")

    # /jobs - Trang tuyển dụng
    @http.route('/jobs', website=True, auth='public')
    def routeJobs(self, **kw):
        jobs = request.env['hr.job'].sudo().search([])
        return request.render("october.page_jobs", {
            'jobs': jobs
        })

    # /job/detail - Trang chi tiết công việc
    @http.route('/job/detail', website=True, auth='public')
    def routeJobDetail(self, **kw):
        return request.render("october.page_job_detail")

    # /job/apply - Trang ứng tuyển
    @http.route('/job/apply', website=True, auth='public')
    def routeJobApply(self, **kw):
        return request.render("october.page_job_apply")

    # /job/thankyou - Trang cảm ơn đã ứng tuyển
    @http.route('/job/thankyou', website=True, auth='public')
    def routeJobThankYou(self, **kw):
        return request.render("october.page_job_thankyou")
    
    # /contact - Trang liên hệ
    @http.route('/contact', website=True, auth='public')
    def routeContact(self, **kw):
        return request.render("october.page_contact")

    # /aboutus - Trang giới thiệu
    @http.route('/aboutus', website=True, auth='public')
    def routeAboutUs(self, **kw):
        return request.render("october.page_aboutus")    