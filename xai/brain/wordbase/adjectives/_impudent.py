

#calss header
class _IMPUDENT():
	def __init__(self,): 
		self.name = "IMPUDENT"
		self.definitions = [u'rude and not showing respect, especially towards someone who is older or in a more important position: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
