/*
 * Name: Hiccupy
 * Version: 1.0
 * Author: thirstscolr@mitchbreathely.org
 *
 * Description: jython binding for Burp Suite.
 */

import java.util.*;
import java.io.*;

import burp.IBurpExtender;
import burp.IBurpExtenderCallbacks;
import burp.IHttpRequestResponse;
import burp.IScanIssue;

import org.python.core.PyObject;
import org.python.util.PythonInterpreter;

public class BurpExtender {
	public IBurpExtenderCallbacks mCallbacks;
	IBurpExtender pyBurpExtender;
	private PyObject pyBurpExtenderClass;
	private Boolean pyApplicationClosing;
	private Boolean pyNewScanIssue;
	private Boolean pyProcessProxyMessage;
	private Boolean pyProcessHttpMessage;
	private Boolean pyRegisterExtenderCallbacks;
	private Boolean pySetCommandLineArgs;

	public BurpExtender() {
		try {
			// initialize the python interpreter object
			PythonInterpreter pyInt = new PythonInterpreter();
			pyInt.exec("import sys");
			pyInt.exec("from BurpExtender import BurpExtender");

			// class introspection to identify supported methods
			pyInt.exec("pyApplicationClosing	= 'applicationClosing' in BurpExtender.__dict__.keys()");
			pyInt.exec("pyNewScanIssue		= 'newScanIssue' in BurpExtender.__dict__.keys()");
			pyInt.exec("pyProcessProxyMessage 	= 'processProxyMessage' in BurpExtender.__dict__.keys()");
			pyInt.exec("pyProcessHttpMessage 	= 'processHttpMessage' in BurpExtender.__dict__.keys()");
			pyInt.exec("pyRegisterExtenderCallbacks = 'registerExtenderCallbacks' in BurpExtender.__dict__.keys()");
			pyInt.exec("pySetCommandLineArgs 	= 'setCommandLineArgs' in BurpExtender.__dict__.keys()");

			// boolean values to dynamically determine method availability
			pyApplicationClosing 	    = (Boolean)pyInt.get("pyApplicationClosing").__tojava__(Boolean.class);
			pyNewScanIssue 		    = (Boolean)pyInt.get("pyNewScanIssue").__tojava__(Boolean.class);
			pyProcessProxyMessage 	    = (Boolean)pyInt.get("pyProcessProxyMessage").__tojava__(Boolean.class);
			pyProcessHttpMessage 	    = (Boolean)pyInt.get("pyProcessHttpMessage").__tojava__(Boolean.class);
			pyRegisterExtenderCallbacks = (Boolean)pyInt.get("pyRegisterExtenderCallbacks").__tojava__(Boolean.class);
			pySetCommandLineArgs 	    = (Boolean)pyInt.get("pySetCommandLineArgs").__tojava__(Boolean.class);
			
			// create a BurpExtender instance and grab a ref to it
			pyBurpExtenderClass = pyInt.get("BurpExtender");
			PyObject pyTmpObject  = pyBurpExtenderClass.__call__();
			pyBurpExtender      = (IBurpExtender)pyTmpObject.__tojava__(IBurpExtender.class);
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public byte[] processProxyMessage(int messageReference,
					  boolean messageIsRequest,
					  String remoteHost,
					  int remotePort,
					  boolean serviceIsHttps,
					  String httpMethod,
					  String url,
					  String resourceType,
					  String statusCode,
					  String responseContentType,
					  byte[] message,
					  int[] interceptAction) {
		if (pyProcessProxyMessage) {
			try {
				return pyBurpExtender.processProxyMessage(messageReference, messageIsRequest, remoteHost, remotePort,
						serviceIsHttps, httpMethod, url, resourceType, statusCode, responseContentType, message,
						interceptAction);
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		return message;
	}

	public void processHttpMessage(String toolName,
				       boolean messageIsRequest,
				       IHttpRequestResponse messageInfo) {
		if (pyProcessHttpMessage) {
			pyBurpExtender.processHttpMessage(toolName, messageIsRequest, messageInfo);
		}
	}

	public void newScanIssue(IScanIssue issue) {
		if (pyNewScanIssue) {
			pyBurpExtender.newScanIssue(issue);
		}
	}

	public void setCommandLineArgs(String[] args) {
		if (pySetCommandLineArgs) {
			pyBurpExtender.setCommandLineArgs(args);
		}
	}

	public void applicationClosing() {
		if (pyApplicationClosing) {
			pyBurpExtender.applicationClosing();
		}
	}

	public void registerExtenderCallbacks(IBurpExtenderCallbacks callbacks) {
		if (pyRegisterExtenderCallbacks) {
			pyBurpExtender.registerExtenderCallbacks(callbacks);
		}
	}

} // BurpExtender
