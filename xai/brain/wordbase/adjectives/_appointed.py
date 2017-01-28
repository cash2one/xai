

#calss header
class _APPOINTED():
	def __init__(self,): 
		self.name = "APPOINTED"
		self.definitions = [u'officially chosen for a job or responsibility: ', u'(of a day or time) arranged for a meeting, etc. to happen: ', u'If buildings or rooms are appointed in a particular way, they have furniture and equipment of the stated standard: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
