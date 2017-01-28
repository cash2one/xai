

#calss header
class _PERMISSIVE():
	def __init__(self,): 
		self.name = "PERMISSIVE"
		self.definitions = [u'A person or society that is permissive allows behaviour that other people might disapprove of: ', u'A permissive path can be used because the owner of the land that it crosses has given permission.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
