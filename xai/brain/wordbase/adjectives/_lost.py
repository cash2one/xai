

#calss header
class _LOST():
	def __init__(self,): 
		self.name = "LOST"
		self.definitions = [u'not knowing where you are and how to get to a place: ', u'If something is lost, no one knows where it is: ', u'not confident and not knowing what to do in a particular situation: ', u'giving so much attention to what you are doing that you are not conscious of anything else that is happening around you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
