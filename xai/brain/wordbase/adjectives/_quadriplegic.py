

#calss header
class _QUADRIPLEGIC():
	def __init__(self,): 
		self.name = "QUADRIPLEGIC"
		self.definitions = [u'permanently unable to move or feel your arms or legs, usually because of a severe injury to the spine (= bones in the centre of the back)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
