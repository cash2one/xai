

#calss header
class _ELECTRONIC():
	def __init__(self,): 
		self.name = "ELECTRONIC"
		self.definitions = [u'(especially of equipment), using, based on, or used in a system of operation that involves the control of electric current by various devices: ', u'relating to computers or something that is done by computers: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
