package com.bacazy.controller;


import com.bacazy.model.JudgeInfomation;
import io.swagger.annotations.Api;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@Api
@RestController("/judge")
public class JudgeController {

    @RequestMapping(method = RequestMethod.GET)
    public JudgeInfomation judge(String json) {
        JudgeInfomation info = new JudgeInfomation();

        return info;
    }
}
