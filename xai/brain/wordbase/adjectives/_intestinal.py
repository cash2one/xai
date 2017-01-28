

#calss header
class _INTESTINAL():
	def __init__(self,): 
		self.name = "INTESTINAL"
		self.definitions = [u'relating to the intestines (= a long tube through which food travels from the stomach and out of the body while it is being digested): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
