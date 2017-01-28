

#calss header
class _FRESH():
	def __init__(self,): 
		self.name = "FRESH"
		self.definitions = [u'new or different: ', u'new and therefore interesting or exciting: ', u'recently made, done, arrived, etc., and especially not yet changed by time: ', u'If you are fresh out of something, you have just finished or sold all of it, so that there is no more left.', u'(of food or flowers) in a natural condition rather than artificially preserved by a process such as freezing: ', u'(of air) clean and cool; found outside rather than in a room: ', u'Fresh weather is cool, sometimes with wind: ', u'clean and pleasant: ', u'energetic, enthusiastic, and not tired: ', u'(of a face) natural, healthy, and young looking: ', u'(of water) not salty: ', u'being too confident and showing no respect, or showing by your actions or words that you want to have sex with someone: ', u'good and attractive or stylish: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
