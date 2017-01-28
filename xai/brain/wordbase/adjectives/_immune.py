

#calss header
class _IMMUNE():
	def __init__(self,): 
		self.name = "IMMUNE"
		self.definitions = [u'protected against a particular disease by particular substances in the blood: ', u'not affected or upset by a particular type of behaviour or emotion: ', u'not able to be punished or damaged by something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
