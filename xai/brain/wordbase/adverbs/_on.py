

#calss header
class _ON():
	def __init__(self,): 
		self.name = "ON"
		self.definitions = [u"on your body or someone's body: ", u'covering the surface of something or connected to something: ', u'used to show when something is operating or starting to operate: ', u'continuing or not stopping: ', u'into a bus, train, plane, etc., or in the correct position to start using some other method of travelling: ', u'performing: ', u'continuing forward in time or space: ', u'happening or planned: ', u'used when talking about the position of one thing compared with the position of another: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
